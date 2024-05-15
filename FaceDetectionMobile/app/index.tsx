import React, { useEffect } from 'react';
import { StyleSheet, TouchableOpacity, View } from 'react-native';
import { Camera, useCameraDevice, useCameraPermission } from 'react-native-vision-camera';


const FaceDetectionMobile: React.FC = () => {
  const { hasPermission, requestPermission } = useCameraPermission();
  // const [faces, setFaces] = React.useState<Face[]>();
  const device = useCameraDevice('front');

  if(!device) return null;

  useEffect(() => {
    if(!hasPermission) {
      requestPermission();
    }
  },[]);

  // const frameProcessor = useFrameProcessor((frame) => {
  //   'worklet';
  //   const scannedFaces = scanFaces(frame);
  //   runOnJS(setFaces)(scannedFaces);
  // }, []);

  // useEffect(() => {
  //   console.log(faces);
  // }, [faces])

  return (
    <View style={styles.camera}>
      <Camera
        style={styles.camera}
        device={device}
        isActive={true}
        // frameProcessor={frameProcessor}
      />
      <TouchableOpacity style={styles.button} />
    </View>
  )
}

const styles = StyleSheet.create({
  camera: {
    flex: 1
  },
  button: {
    position: 'absolute',
    borderRadius: 50,
    width: 100,
    height: 100,
    bottom: 20,
    left: '37%',
    backgroundColor: 'rgba(0,0,0,0.2)',
    borderColor: 'rgba(0,0,0,0.5)',
    borderWidth: 3,
    borderStyle: 'dashed',
  }
})

export default FaceDetectionMobile;