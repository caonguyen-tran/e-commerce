import {
  View,
  Text,
  Button,
  TextInput,
  Pressable,
  TouchableOpacity,
  Image,
  ScrollView,
} from "react-native";
import UserStyle from "./UserStyle";
import { MaterialCommunityIcons } from "@expo/vector-icons";
import { useState } from "react";

const Register = ({ navigation }) => {
  const [info, setInfo] = useState({
    firstname: "",
    lastname: "",
    email: "",
    phone: "",
    password: "",
    confirm_password: "",
  });
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  const change = (field, value) => {
    setInfo((current) => {
      return { ...current, [field]: value };
    });
  };
  return (
    <View style={UserStyle.container}>
      <View>
        <Text style={UserStyle.headerText}>Login Account</Text>
        <Text style={{ fontSize: 16, color: "#818181" }}>
          Create account to continue shopping with tnEC
        </Text>
      </View>

      <ScrollView
        style={UserStyle.inputContainer}
        showsVerticalScrollIndicator={false}
        alwaysBounceHorizontal={false}
        >
        <View style={UserStyle.inputView}>
          <TextInput
            value={info.firstname}
            placeholder="Firstname"
            style={UserStyle.textInput}
            onChangeText={(t) => {
              change("firstname", t);
            }}
          />
        </View>
        <View style={UserStyle.inputView}>
          <TextInput
            value={info.lastname}
            placeholder="Lastname"
            style={UserStyle.textInput}
            onChangeText={(t) => change("lastname", t)}
          />
        </View>
        <View style={UserStyle.inputView}>
          <TextInput
            value={info.lastname}
            placeholder="Lastname"
            style={UserStyle.textInput}
            onChangeText={(t) => change("lastname", t)}
          />
        </View>
        <View style={UserStyle.inputView}>
          <TextInput
            value={info.lastname}
            placeholder="Lastname"
            style={UserStyle.textInput}
            onChangeText={(t) => change("lastname", t)}
          />
        </View>
        <View style={UserStyle.inputView}>
          <TextInput
            value={info.username}
            placeholder="Username"
            style={UserStyle.textInput}
            onChangeText={(t) => change("username", t)}
          />
        </View>

        <View style={UserStyle.inputView}>
          <TextInput
            value={info.password}
            secureTextEntry={!showPassword}
            placeholder="Password"
            style={UserStyle.textInput}
            onChangeText={(t) => change("password", t)}
          />

          <Pressable
            onPress={() => {
              setShowPassword(!showPassword);
            }}
          >
            <MaterialCommunityIcons
              name={!showPassword ? "eye-off" : "eye"}
              size={22}
              color="#232323"
              style={{ marginLeft: 20 }}
            />
          </Pressable>
        </View>

        <View style={UserStyle.inputView}>
          <TextInput
            value={info.confirm_password}
            secureTextEntry={!showConfirmPassword}
            placeholder="Confirm password"
            style={UserStyle.textInput}
            onChangeText={(t) => change("confirm_password", t)}
          />

          <Pressable
            onPress={() => {
              setShowConfirmPassword(!showConfirmPassword);
            }}
          >
            <MaterialCommunityIcons
              name={!showConfirmPassword ? "eye-off" : "eye"}
              size={22}
              color="#232323"
              style={{ marginLeft: 20 }}
            />
          </Pressable>
        </View>
        <TouchableOpacity
          style={UserStyle.loginButton}
          onPress={() => navigation.navigate("Register")}
        >
          <Text
            style={{
              fontSize: 24,
              color: "#fff",
              fontWeight: "600",
              lineHeight: 50,
            }}
          >
            Register Now
          </Text>
        </TouchableOpacity>
        <View
          style={{
            flexDirection: "row",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Text style={{ fontSize: 16, color: "#818181" }}>
            All ready have an Account?
          </Text>
          <Pressable
            onPress={() => {
              navigation.navigate("Login");
            }}
          >
            <Text style={{ fontSize: 16, fontWeight: 700, color: "steelblue" }}>
              {" "}
              Sign in
            </Text>
          </Pressable>
        </View>
        <View
          style={{
            flexDirection: "row",
            alignItems: "center",
            marginVertical: 40,
          }}
        >
          <View style={{ flex: 1, height: 1, backgroundColor: "black" }} />
          <View>
            <Text style={{ width: 50, textAlign: "center" }}>OR</Text>
          </View>
          <View style={{ flex: 1, height: 1, backgroundColor: "black" }} />
        </View>
        <View
          style={{
            flexDirection: "row",
            alignItems: "center",
            justifyContent: "center",
            paddingBottom: 60
          }}
        >
          <Pressable onPress={() => {}}>
            <Image
              source={{
                uri: "https://res.cloudinary.com/dndakokcz/image/upload/v1706947907/google_qk8s0c.jpg",
              }}
              style={UserStyle.imageStyle}
            />
          </Pressable>
          <Pressable onPress={() => {}}>
            <Image
              source={{
                uri: "https://res.cloudinary.com/dndakokcz/image/upload/v1706947906/facebook_axwuyw.png",
              }}
              style={UserStyle.imageStyle}
            />
          </Pressable>
          <Pressable onPress={() => {}}>
            <Image
              source={{
                uri: "https://res.cloudinary.com/dndakokcz/image/upload/v1706947965/discord_v6dvbt.png",
              }}
              style={UserStyle.imageStyle}
            />
          </Pressable>
        </View>
        </ScrollView>
    </View>
  );
};

export default Register;
