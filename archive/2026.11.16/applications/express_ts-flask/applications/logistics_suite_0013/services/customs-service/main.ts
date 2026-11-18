import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { declareCustoms } from "./customs_declare";
import { mergeShipment } from "./merge_shipment";
import { renderProfile } from "./render_profile";
import { enrichCheckpoint } from "./enrich_checkpoint";
import { reconcileSnapshot } from "./reconcile_snapshot";
import { exportSummary } from "./export_summary";
import { enrichReport } from "./enrich_report";
import { loadIndex } from "./load_index";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/declareCustoms", route(declareCustoms));
app.post("/mergeShipment", route(mergeShipment));
app.post("/renderProfile", route(renderProfile));
app.post("/enrichCheckpoint", route(enrichCheckpoint));
app.post("/reconcileSnapshot", route(reconcileSnapshot));
app.post("/exportSummary", route(exportSummary));
app.post("/enrichReport", route(enrichReport));
app.post("/loadIndex", route(loadIndex));

app.listen(3000, "0.0.0.0");
