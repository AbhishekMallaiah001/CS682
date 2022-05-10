
Alfred workflow of the PVI data and display the PVI data of the current location in weather workflow fashion :

STEP 1 :   Create a blank workflow in alfred, please find the below image for reference 

![Image 5-9-22 at 7 31 PM](https://user-images.githubusercontent.com/78864285/167522571-127a3618-6e0b-4d0b-b3fa-75b7e7a80719.JPG)

STEP 2 :  Fill the data in Blank workflow dialogue box as follows 

![Image 5-9-22 at 7 33 PM](https://user-images.githubusercontent.com/78864285/167522944-3fbc7e96-6804-439a-85f5-dfc851dcf91f.JPG)

STEP 3:  Create a script filter, follow the below screenshot

![Image 5-9-22 at 7 34 PM](https://user-images.githubusercontent.com/78864285/167523034-f659cc8f-cbd5-458b-9bc2-720f76c48de8.JPG)

STEP 4:  Fill the script filter dialogue box as follows 

![Image 5-9-22 at 7 34 PM (1)](https://user-images.githubusercontent.com/78864285/167523186-d3325e5e-66f1-46c7-b20a-c0a278343eca.JPG)

STEP 5: Right-Click on the workflow and select the "open in finder" and copy the files uploaded on this github, to the folder

![Image 5-9-22 at 7 35 PM](https://user-images.githubusercontent.com/78864285/167523342-8d3e317a-b7a3-4dda-9bae-df063a53f237.JPG)

STEP 6: Right-Click on the workflow as the above image and select "open in terminal" (Below the "open in finder"). and install the below mentioned packages 
       requests , geocoder , datetime , json , csv using the cmd  " pip3 install --target=. <PACKAGE_NAME> "
       
STEP 7: Then type "pvid" on the alfred toggle" (serach bar) you can see the below output.

" First 9 Rows of output"
![Image 5-9-22 at 7 49 PM](https://user-images.githubusercontent.com/78864285/167523828-b78ec8c6-00bc-4920-bae0-5b38c276b73d.JPG)

" Rest of the Rows"
![Image 5-9-22 at 7 49 PM (1)](https://user-images.githubusercontent.com/78864285/167523854-048221b7-0391-4406-9a8d-d7125d47e7ac.JPG)

