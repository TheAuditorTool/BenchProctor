import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { runConversion } from "./convert_job";
import { annotateBundle } from "./annotate_bundle";
import { normalizeSnapshot } from "./normalize_snapshot";
import { rotateReceipt } from "./rotate_receipt";
import { fetchThreshold } from "./fetch_threshold";
import { buildCheckpoint } from "./build_checkpoint";
import { annotateHeader } from "./annotate_header";
import { reconcileBundle } from "./reconcile_bundle";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/runConversion", runConversion);
app.post("/annotateBundle/:id", annotateBundle);
app.post("/normalizeSnapshot", normalizeSnapshot);
app.post("/rotateReceipt", rotateReceipt);
app.post("/fetchThreshold", fetchThreshold);
app.post("/buildCheckpoint", buildCheckpoint);
app.post("/annotateHeader", annotateHeader);
app.post("/reconcileBundle", reconcileBundle);

app.listen(3000, "0.0.0.0");
