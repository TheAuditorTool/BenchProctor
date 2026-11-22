import express, { Request, Response } from "express";
import session from "express-session";

import { ingestMetric } from "./metric_ingest";
import { archiveReceipt } from "./archive_receipt";
import { reconcileSample } from "./reconcile_sample";
import { mergeReport } from "./merge_report";
import { reconcileSchedule } from "./reconcile_schedule";
import { resolveWindow } from "./resolve_window";
import { rotateDigest } from "./rotate_digest";
import { mergeReceipt } from "./merge_receipt";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/ingestMetric", ingestMetric);
app.post("/archiveReceipt", archiveReceipt);
app.post("/reconcileSample", reconcileSample);
app.post("/mergeReport", mergeReport);
app.post("/reconcileSchedule", reconcileSchedule);
app.post("/resolveWindow", resolveWindow);
app.post("/rotateDigest", rotateDigest);
app.post("/mergeReceipt/:id", mergeReceipt);

app.listen(3000, "0.0.0.0");
