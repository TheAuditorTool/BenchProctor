import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { configureSample } from "./sample_config";
import { fetchConfig } from "./fetch_config";
import { annotateReport } from "./annotate_report";
import { compactIndex } from "./compact_index";
import { reconcileThreshold } from "./reconcile_threshold";
import { enrichSchedule } from "./enrich_schedule";
import { renderBundle } from "./render_bundle";
import { collectSample } from "./collect_sample";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/configureSample", route(configureSample));
app.post("/fetchConfig", route(fetchConfig));
app.post("/annotateReport", route(annotateReport));
app.post("/compactIndex", route(compactIndex));
app.post("/reconcileThreshold/:id", route(reconcileThreshold));
app.post("/enrichSchedule", route(enrichSchedule));
app.post("/renderBundle", route(renderBundle));
app.post("/collectSample", route(collectSample));

app.listen(3000, "0.0.0.0");
