/**
 * React 應用程式的入口點
 * 
 * 此檔案負責初始化 React 應用程式，並將其掛載到 DOM 中。
 * 
 * @module main
 * 
 * @example
 * // 應用程式啟動時會執行此檔案
 * // 1. 匯入必要的 React 函數和元件
 * // 2. 獲取 HTML 中 id 為 'root' 的元素
 * // 3. 使用 StrictMode 包裝 App 元件以檢測潛在問題
 * // 4. 將應用程式渲染到該元素中
 */
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
