package com.example.prefgrade;

import android.os.Bundle;
import android.widget.Button;
import android.view.View;
import android.content.Intent;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {
    Button insightsButton;
    Button dataDescriptButton;
    Button graphsButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);


        dataDescriptButton = findViewById(R.id.dataset);
        dataDescriptButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, DatasetDescript.class);
                startActivity(intent);
            }
        });

        insightsButton = findViewById(R.id.statistical);
        insightsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, StatisticalInsights.class);
                startActivity(intent);
            }
        });

        graphsButton = findViewById(R.id.graphs_btn);
        graphsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, Graphs.class);
                startActivity(intent);
            }
        });
        WindowCompat.setDecorFitsSystemWindows(getWindow(), false);
        // Apply insets to button container
        View buttonContainer = findViewById(R.id.button_container);
        ViewCompat.setOnApplyWindowInsetsListener(buttonContainer, (v, insets) -> {
            Insets bars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(v.getPaddingLeft(), bars.top, v.getPaddingRight(), bars.bottom);
            return insets;
        });
    }
}