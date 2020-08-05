# Terrific-Traffic

Terrific Traffic is a web-based Traffic Anomaly Detection System in which the YOLOv3 Object Detection Model is tranied on a combination of 2 datasets, AI City Challenge 2019 (Track 3) and DETRAC.

The web application is developed in Flask and plain Javascript alongwith HTML, CSS, and Bootstrap.

You need to download the yolov3_6000.weights file from this [link](https://drive.google.com/file/d/15fr1grDWgV4u_JCX9QuTM8uhSfNSHdXF/view?usp=sharing) and save the file in the [yolo directory](./yolo/)

## Usage

- First, you need to navigate to the project folder and run this line in command prompt,

```bash
python app.py 
```
The web application will run on ``` 127.0.0.1:5000 ```.

- The web application will need a signup. There is already a database, ```tutorial.db```, made with some credentials specified in the file [dummy.py](./dummy.py). So you can either login with the hard coded credentials or define your own in the file.

- After login is successful, you will be redirected to another page where you need to choose a file with an ```mp4``` format. 

**Note: Before selecting a video file, bear in mind that any video you choose must be inside the [videos directory](./videos/)**

You would also need to change the ```directory_path``` variable in the [app.py](./app.py) file on line number ```81```

- After you submit the file that you chose, there will be a delay in redirecting to the next page where you would be able to play the video after detection. The duration of the delay depends on the size of the video file you chose. You can also see how long it will take in the command prompt running in the background.

- As the processing is done, you will be redirected to the next page where you can play the processed video and also save the frames at any instance of the playing video by clicking on the **Save Frame** button. The saved frames will appear below the video and you can right click and save them on your system if you need to.
