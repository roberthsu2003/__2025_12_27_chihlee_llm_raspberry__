import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React - HMR 測試</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          點擊次數:{count}
        </button>
        <p>
          已修改 App.tsx，請存檔觀察是否立即熱更新(HOT MODULE REPLACEMENT)，不需重新整理頁面。
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
