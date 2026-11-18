import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { sweepRetention } from "./retention_sweep";
import { rotateCheckpoint } from "./rotate_checkpoint";
import { validateCheckpoint } from "./validate_checkpoint";
import { compactBatch } from "./compact_batch";
import { archiveSchedule } from "./archive_schedule";
import { annotateHeader } from "./annotate_header";
import { collectReport } from "./collect_report";
import { fetchThreshold } from "./fetch_threshold";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/sweepRetention", route(sweepRetention));
app.post("/rotateCheckpoint", route(rotateCheckpoint));
app.post("/validateCheckpoint", route(validateCheckpoint));
app.post("/compactBatch", route(compactBatch));
app.post("/archiveSchedule", route(archiveSchedule));
app.post("/annotateHeader", route(annotateHeader));
app.post("/collectReport", route(collectReport));
app.post("/fetchThreshold", route(fetchThreshold));

app.listen(3000, "0.0.0.0");
