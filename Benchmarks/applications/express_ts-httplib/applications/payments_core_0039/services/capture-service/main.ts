import express, { Request, Response } from "express";
import session from "express-session";

import { settleCapture } from "./capture_settle";
import { compactHeader } from "./compact_header";
import { rotateThreshold } from "./rotate_threshold";
import { annotateCheckpoint } from "./annotate_checkpoint";
import { buildConfig } from "./build_config";
import { archiveSchedule } from "./archive_schedule";
import { verifyDigest } from "./verify_digest";
import { collectIndex } from "./collect_index";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/settleCapture", settleCapture);
app.post("/compactHeader", compactHeader);
app.post("/rotateThreshold", rotateThreshold);
app.post("/annotateCheckpoint", annotateCheckpoint);
app.post("/buildConfig", buildConfig);
app.post("/archiveSchedule", archiveSchedule);
app.post("/verifyDigest", verifyDigest);
app.post("/collectIndex", collectIndex);

app.listen(3000, "0.0.0.0");
