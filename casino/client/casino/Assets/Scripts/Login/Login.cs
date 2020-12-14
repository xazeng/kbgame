using System;
using KBEngine;
using UnityEngine;
using UnityEngine.UI;

namespace Login
{
    public class Login : MonoBehaviour
    {
        private void Start()
        {
            
        }

        private void Update()
        {
            
        }

        public void StartLogin()
        {
            //账号密码都要大于6位
            //得到账户输入框的文本
            string account = GameObject.Find("UserNameInput").GetComponent<InputField>().text;
            //得到密码输入框的文本
            string password = GameObject.Find("PasswordInput").GetComponent<InputField>().text;
            //调用API的登录接口。最后一个参数可暂时无视，具体请参考API手册
            KBEngineApp.getSingleton().login(account, password, System.Text.Encoding.UTF8.GetBytes("casino"));
        }
    }
}