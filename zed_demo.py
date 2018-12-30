import pyzed.sl as sl
import math
import numpy as np
import sys
import cv2

def main():


    closed_cascadeV3 = cv2.CascadeClassifier('road_closed_v3.xml')
    ow_left_cascade = cv2.CascadeClassifier('ow_left_arrow.xml')
    ow_right_cascade = cv2.CascadeClassifier('ow_right_arrow.xml')
    stop_cascade = cv2.CascadeClassifier('stopsign_classifier.xml')
    no_left_cascade = cv2.CascadeClassifier('no_trun_left_symbol_v2.xml')
    no_right_cascade = cv2.CascadeClassifier('no_turn_right.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX


    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_PERFORMANCE  # Use PERFORMANCE depth mode
    init_params.coordinate_units = sl.UNIT.UNIT_MILLIMETER  # Use milliliter units (for depth measurements)

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    # Create and set RuntimeParameters after opening the camera
    runtime_parameters = sl.RuntimeParameters()
    runtime_parameters.sensing_mode = sl.SENSING_MODE.SENSING_MODE_STANDARD  # Use STANDARD sensing mode

    # Capture 50 images and depth, then stop
    #i = 0
    image = sl.Mat()
    depth = sl.Mat()
    point_cloud = sl.Mat()

    while 1:
        # A new image is available if grab() returns SUCCESS
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # Retrieve left image
            zed.retrieve_image(image, sl.VIEW.VIEW_LEFT)
            # Retrieve depth map. Depth is aligned on the left image
            zed.retrieve_measure(depth, sl.MEASURE.MEASURE_DEPTH)
            # Retrieve colored point cloud. Point cloud is aligned on the left image.
            zed.retrieve_measure(point_cloud, sl.MEASURE.MEASURE_XYZRGBA)


            ow_left_signs = ow_left_cascade.detectMultiScale(gray) 
            ow_right_signs= ow_right_cascade.detectMultiScale(gray)
            closed_signsV3 = closed_cascadeV3.detectMultiScale(gray)
            stop_signs = stop_cascade.detectMultiScale(gray)
            no_left_signs = no_left_cascade.detectMultiScale(gray,1.5,2)
            no_right_signs = no_right_cascade.detectMultiScale(gray,1.5,2)

            for (x,y,w,h) in closed_signsV3:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                # cv2.putText(img,'Road Closed V3',(x+w,y+h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
                err, point_cloud_value = point_cloud.get_value(x, y)

                distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
                                     point_cloud_value[1] * point_cloud_value[1] +
                                     point_cloud_value[2] * point_cloud_value[2])

                if not np.isnan(distance) and not np.isinf(distance):
                    distance = round(distance)
                    cv2.putText(img,'Road Closed V3 ' + distance,(x+w,y+h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
                    # print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
                else:
                    print("Can't estimate distance at this position, move the camera\n")
                sys.stdout.flush()


            for (x,y,w,h) in ow_right_signs:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                # cv2.putText(img,'One Way Right',(x+w,y+h), font, 0.5, (0,255,0), 2, cv2.LINE_AA)
                err, point_cloud_value = point_cloud.get_value(x, y)

                distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
                                     point_cloud_value[1] * point_cloud_value[1] +
                                     point_cloud_value[2] * point_cloud_value[2])

                if not np.isnan(distance) and not np.isinf(distance):
                    distance = round(distance)
                    # print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
                else:
                    print("Can't estimate distance at this position, move the camera\n")
                sys.stdout.flush()

            
            for (x,y,w,h) in ow_left_signs:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                # cv2.putText(img,'One Way Left',(x+w,y+h), font, 0.5, (0,255,0), 2, cv2.LINE_AA)
                err, point_cloud_value = point_cloud.get_value(x, y)

                distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
                                     point_cloud_value[1] * point_cloud_value[1] +
                                     point_cloud_value[2] * point_cloud_value[2])

                if not np.isnan(distance) and not np.isinf(distance):
                    distance = round(distance)
                    cv2.putText(img,'One Way Left',(x+w,y+h), font, 0.5, (0,255,0), 2, cv2.LINE_AA)
                    # print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
                else:
                    print("Can't estimate distance at this position, move the camera\n")
                sys.stdout.flush()


            for (x,y,w,h) in stop_signs:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                # cv2.putText(img,'Stop Sign',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
                err, point_cloud_value = point_cloud.get_value(x, y)

                distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
                                     point_cloud_value[1] * point_cloud_value[1] +
                                     point_cloud_value[2] * point_cloud_value[2])

                if not np.isnan(distance) and not np.isinf(distance):
                    distance = round(distance)
                    cv2.putText(img,'Stop Sign',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
                    # print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
                else:
                    print("Can't estimate distance at this position, move the camera\n")
                sys.stdout.flush()

            
            for (x,y,w,h) in no_left_signs:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                # cv2.putText(img,'No Turn Left',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
                err, point_cloud_value = point_cloud.get_value(x, y)

                distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
                                     point_cloud_value[1] * point_cloud_value[1] +
                                     point_cloud_value[2] * point_cloud_value[2])

                if not np.isnan(distance) and not np.isinf(distance):
                    distance = round(distance)
                    cv2.putText(img,'No Turn Left',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
                    # print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
                else:
                    print("Can't estimate distance at this position, move the camera\n")
                sys.stdout.flush()


            for (x,y,w,h) in no_right_signs:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                # cv2.putText(img,'No Turn Right',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
                err, point_cloud_value = point_cloud.get_value(x, y)

                distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
                                     point_cloud_value[1] * point_cloud_value[1] +
                                     point_cloud_value[2] * point_cloud_value[2])

                if not np.isnan(distance) and not np.isinf(distance):
                    distance = round(distance)
                    cv2.putText(img,'No Turn Right',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
                    # print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
                else:
                    print("Can't estimate distance at this position, move the camera\n")
                sys.stdout.flush()


            # Get and print distance value in mm at the center of the image
            # We measure the distance camera - object using Euclidean distance
            # x = round(image.get_width() / 2)
            # y = round(image.get_height() / 2)
            # err, point_cloud_value = point_cloud.get_value(x, y)

            # distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
            #                      point_cloud_value[1] * point_cloud_value[1] +
            #                      point_cloud_value[2] * point_cloud_value[2])

            # if not np.isnan(distance) and not np.isinf(distance):
            #     distance = round(distance)
            #     print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
            
            # else:
            #     print("Can't estimate distance at this position, move the camera\n")
            # sys.stdout.flush()

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
            if cv2.getWindowProperty('img',cv2.WND_PROP_VISIBLE) < 1:        
                break      

    # Close the camera
    zed.close()

if __name__ == "__main__":
    main()