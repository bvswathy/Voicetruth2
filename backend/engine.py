

import wave
import numpy as np

def read_audio(path):

    with wave.open(path, 'rb') as f:
        frames = f.readframes(-1)
        y = np.frombuffer(frames, dtype=np.int16)

    return y


def behaviour_score(path):

    y = read_audio(path)

    # 1. Stability
    stability = np.std(y[:2000])

    # 2. Zero pattern
    zcr = np.mean(np.abs(np.diff(np.sign(y))))

    # 3. Energy smoothness
    energy = np.mean(np.abs(y))

    score = (
        (1/(stability+1))*0.4 +
        zcr*0.3 +
        (1/(energy+1))*0.3
    )

    return float(score)


def decide(score):

    if score > 0.6:
        return "HUMAN", 0.84
    else:
        return "AI_GENERATED", 0.88
