import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { quoteShipment } from "./shipment_quote";
import { auditWindow } from "./audit_window";
import { collectSummary } from "./collect_summary";
import { rotateCheckpoint } from "./rotate_checkpoint";
import { enrichBundle } from "./enrich_bundle";
import { exportRoster } from "./export_roster";
import { formatPolicy } from "./format_policy";
import { enrichRoster } from "./enrich_roster";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/quoteShipment", route(quoteShipment));
app.post("/auditWindow/:id", route(auditWindow));
app.post("/collectSummary", route(collectSummary));
app.post("/rotateCheckpoint", route(rotateCheckpoint));
app.post("/enrichBundle", route(enrichBundle));
app.post("/exportRoster", route(exportRoster));
app.post("/formatPolicy", route(formatPolicy));
app.post("/enrichRoster", route(enrichRoster));

app.listen(3000, "0.0.0.0");
