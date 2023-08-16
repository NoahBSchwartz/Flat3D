# 3D-Screen-Illusion
This is code that was created to compete in the TSA Software Development Competition. I saw an article about Google's new screen that made video look 3D by tracking the user's face and moving the video based on their head movements. I thought it might be possible to get this same result on a normal laptop by using the Mediapipe face tracking code (https://google.github.io/mediapipe/solutions/face_mesh.html) to move a Blender scene based on where I was in the frame. The challenging part of the project was getting the Mediapipe code to interact with Blender at a convincing frame rate. Because they both relied on different Python versions, I ended up using socket communication to send the data to Blender which then and angled the camera. 

<p align="center">
  <img src="https://github.com/NoahBSchwartz/3D-Screen-Illusion/assets/44248582/aa768b78-3afc-43e2-9aa0-c05c6392af67" alt="unnamed (1)" width="250"/>
  <br>
  <img src="https://github.com/NoahBSchwartz/3D-Screen-Illusion/assets/arrow.png" alt="arrow" height="500"/>
  <br>
  <img src="https://github.com/NoahBSchwartz/3D-Screen-Illusion/assets/44248582/054dbea0-516c-42d0-94dc-0b7e4efcdcaa" alt="unnamed" width="250"/>
  <br>
  <img src="https://github.com/NoahBSchwartz/3D-Screen-Illusion/assets/arrow.png" alt="arrow" height="500"/>
  <br>
  <img src="https://github.com/NoahBSchwartz/3D-Screen-Illusion/assets/44248582/5ddadec2-3c3f-4239-b3b5-2ff5bb0fe103" alt="unnamed (2)" width="250"/>
</p>
