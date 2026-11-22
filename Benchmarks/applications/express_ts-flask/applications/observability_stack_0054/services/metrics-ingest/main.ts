import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { ingestMetric } from "./metric_ingest";
import { validateAlert } from "./validate_alert";
import { enrichReport } from "./enrich_report";
import { buildThreshold } from "./build_threshold";
import { archiveIndex } from "./archive_index";
import { resolveBundle } from "./resolve_bundle";
import { renderCheckpoint } from "./render_checkpoint";
import { rotateThreshold } from "./rotate_threshold";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/ingestMetric", route(ingestMetric));
app.post("/validateAlert", route(validateAlert));
app.post("/enrichReport", route(enrichReport));
app.post("/buildThreshold", route(buildThreshold));
app.post("/archiveIndex", route(archiveIndex));
app.post("/resolveBundle", route(resolveBundle));
app.post("/renderCheckpoint", route(renderCheckpoint));
app.post("/rotateThreshold", route(rotateThreshold));

app.listen(3000, "0.0.0.0");
