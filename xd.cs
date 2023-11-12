using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class xd : MonoBehaviour
{
    //хп
    int health = 5;
    //уровнь
    int level = 1;
    //скорость
    float speed = 1.2f;
    // Start is called before the first frame 
    void Start()
    {
        health = health + level;
        print(health);
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 newPosition = transform.position;
        newPosition.z += speed * Time.deltaTime;
        transform.position = newPosition;
    }
}
