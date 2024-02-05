import {
  View,
  Text,
  Button,
  TextInput,
  Pressable,
  TouchableOpacity,
  Image,
} from "react-native";
import UserStyle from "./UserStyle";
import { MaterialCommunityIcons } from "@expo/vector-icons";
import { useState } from "react";
import API, { endpoints, authApi } from "../../configs/API";
import AsyncStorage from "@react-native-async-storage/async-storage";

const Login = ({ navigation }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isVisible, setIsVisible] = useState(false);
  const [error, setError] = useState("");
  const focus = () => {
    setError('')
  }
  const login = async () => {
    try {
      let res = await API.get(endpoints['shops'])
      console.log(res.data)
      // const res = await API.post(endpoints["login"], {
      //   "username": username,
      //   "password": password,
      //   "client_id": "AdxxO1AhG2coA6FfW3pUOUmL494g3jGM39jkQMeM",
      //   "client_secret":
      //     "T7gZuzyYKKn2YEvqKDAFt2MD9DzvwFVyDvuqLI21GMFSMFi59cOnxV4rfDnSLT8oIVEl5zmf1ZUGZ1iBWa23ePIHQctsojjIYbsM9DAHQrkrPK0VeDInJG1YqwNH7IYv",
      //   "grant_type": "password",
      // });
      // await AsyncStorage.setItem("access-token", res.data.access_token);
      // let user = await authApi(res.data.access_token).get(
      //   endpoints["current-user"]
      // );
      // dispatch({
      //   type: "login",
      //   payload: user.data,
      // });
      // navigation.navigate("Home");
    } catch (ex) {
      setError("Username or password incorrect!");
    }
  };
  return (
    <View style={UserStyle.container}>
      <View>
        <Text style={UserStyle.headerText}>Login Account</Text>
        <Text style={{ fontSize: 16, color: "#818181" }}>
          Enter your username and password to login
        </Text>
      </View>

      <View style={UserStyle.inputContainer}>
        <Text style={{ fontSize: 16, color: "red", fontWeight: "600" }}>
          {error}
        </Text>
        <View style={UserStyle.inputView}>
          <TextInput
            value={username}
            placeholder="Username"
            style={UserStyle.textInput}
            onChangeText={setUsername}
            onFocus={focus}
          />
        </View>

        <View style={UserStyle.inputView}>
          <TextInput
            value={password}
            secureTextEntry={!isVisible}
            placeholder="Password"
            style={UserStyle.textInput}
            onChangeText={setPassword}
          />

          <Pressable
            onPress={() => {
              setIsVisible(!isVisible);
            }}
          >
            <MaterialCommunityIcons
              name={!isVisible ? "eye-off" : "eye"}
              size={22}
              color="#232323"
              style={{ marginLeft: 20 }}
            />
          </Pressable>
        </View>
        <Pressable
          style={{
            paddingVertical: 8,
            flexDirection: "row",
            justifyContent: "flex-end",
          }}
          onPress={() => {}}
        >
          <Text style={{ color: "steelblue", fontWeight: "800" }}>
            Forgot password ?
          </Text>
        </Pressable>
        <TouchableOpacity
          style={UserStyle.loginButton}
          onPress={login}
        >
          <Text
            style={{
              fontSize: 24,
              color: "#fff",
              fontWeight: "600",
              lineHeight: 50,
            }}
          >
            Login
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
            Dont't have an Account?
          </Text>
          <Pressable
            onPress={() => {
              navigation.navigate("Register");
            }}
          >
            <Text style={{ fontSize: 16, fontWeight: 700, color: "steelblue" }}>
              {" "}
              Sign up
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
      </View>
    </View>
  );
};

export default Login;
