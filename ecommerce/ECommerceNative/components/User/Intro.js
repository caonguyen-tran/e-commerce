import { View, Text, Button, StyleSheet, TouchableOpacity, Image } from "react-native";
import Login from "./Login";

const Intro = function({navigation}){
  return (
    <View style={IntroStyle.container}>
        <Image style={IntroStyle.imageStyle} source={{uri: "https://res.cloudinary.com/dndakokcz/image/upload/v1706892359/logoapp_x3qzxq.jpg"}} />
        <TouchableOpacity style={IntroStyle.btnStyle} onPress={() => navigation.navigate('Login')}>
            <Text style={IntroStyle.textStyle}>
                Get Started
            </Text>
        </TouchableOpacity>
    </View>
  );
};

const IntroStyle = StyleSheet.create({
    container: {
        height: "100%",
        justifyContent: "space-between",
        alignItems: "center",
        backgroundColor: "#fff"
    },
    btnStyle: {
        backgroundColor: "steelblue",
        width: "92%",
        height: 56,
        borderRadius: 7,
        marginBottom: 24
    },
    textStyle: {
        fontSize: 20,
        color: "#fff",
        textAlign: "center",
        lineHeight: 56,
        fontWeight: "600"
    },
    imageStyle: {
        width: 300,
        height: 300,
        marginTop: 200
    }
})

export default Intro;
