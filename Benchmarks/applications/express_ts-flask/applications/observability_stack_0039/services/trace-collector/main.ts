import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { collectTrace } from "./trace_collect";
import { reconcileSnapshot } from "./reconcile_snapshot";
import { rotateBundle } from "./rotate_bundle";
import { renderReport } from "./render_report";
import { enrichTrace } from "./enrich_trace";
import { reconcileRoster } from "./reconcile_roster";
import { exportWindow } from "./export_window";
import { reconcileBatch } from "./reconcile_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/collectTrace", route(collectTrace));
app.post("/reconcileSnapshot", route(reconcileSnapshot));
app.post("/rotateBundle", route(rotateBundle));
app.post("/renderReport", route(renderReport));
app.post("/enrichTrace", route(enrichTrace));
app.post("/reconcileRoster", route(reconcileRoster));
app.post("/exportWindow", route(exportWindow));
app.post("/reconcileBatch", route(reconcileBatch));

app.listen(3000, "0.0.0.0");
