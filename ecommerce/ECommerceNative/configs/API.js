import axios from "axios";


export const endpoints = {
    'login': '/o/token/',
    'register': '/user/',
    'create-shop': '/user/create-shop/',
    'current-user': '/user/current-user/',
    'categories' :'/categories/',
    'cart': '/cart/',
    'checkout': '/cart/checkout/',
    'remove-product': (product_id) => `cart/${product_id}/remove-product/`,
    'products' : '/product/',
    'product-details': (product_id) => `/product/${product_id}/`,
    'update-product': (product_id) => `product/${product_id}/`,
    'delete-product': (product_id) => `product/${product_id}/`,
    'add-cart': (product_id) => `/product/${product_id}/add-cart/`,
    'shops': '/shop/',
    'shop-details': (shop_id) => `/shop/${shop_id}/`,
    'delete-shop': (shop_id) => `/shop/${shop_id}/`,
    'add-product-to-shop': (shop_id) => `/shop/${shop_id}/add-product/`,
    'confirm-shop': (shop_id) => `/shop/${shop_id}/confirm/` // only admin or staff

}

export const authApi = (accessToken) => axios.create({
    baseURL: "http://127.0.0.1:8000",
    headers: {
        Authorization: `Bearer ${accessToken}`
    }
})

export default axios.create({
    baseURL: "http://127.0.0.1:8000"
})



