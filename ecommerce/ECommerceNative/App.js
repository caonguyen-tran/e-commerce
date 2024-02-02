import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Home from './components/Home/Home';
import Product from './components/Products/Product';

const Drawer = createDrawerNavigator()
export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Screen name='Drawer 1' component={Home}/> 
      <Drawer.Screen  name ='Drawer 2' component={Product}/>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
