import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { pollTracking } from "./tracking_poll";
import { buildRecord } from "./build_record";
import { rotateLabel } from "./rotate_label";
import { compactPolicy } from "./compact_policy";
import { auditBatch } from "./audit_batch";
import { collectProfile } from "./collect_profile";
import { compactThreshold } from "./compact_threshold";
import { archiveRecord } from "./archive_record";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/pollTracking", route(pollTracking));
app.post("/buildRecord", route(buildRecord));
app.post("/rotateLabel", route(rotateLabel));
app.post("/compactPolicy", route(compactPolicy));
app.post("/auditBatch", route(auditBatch));
app.post("/collectProfile", route(collectProfile));
app.post("/compactThreshold", route(compactThreshold));
app.post("/archiveRecord", route(archiveRecord));

app.listen(3000, "0.0.0.0");
