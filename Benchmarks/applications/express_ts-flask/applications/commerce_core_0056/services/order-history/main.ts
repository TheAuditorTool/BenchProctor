import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { lookupOrder } from "./order_lookup";
import { verifyWindow } from "./verify_window";
import { archivePolicy } from "./archive_policy";
import { resolveBundle } from "./resolve_bundle";
import { enrichReport } from "./enrich_report";
import { validateThreshold } from "./validate_threshold";
import { compactRoster } from "./compact_roster";
import { verifyOrder } from "./verify_order";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/lookupOrder", route(lookupOrder));
app.post("/verifyWindow", route(verifyWindow));
app.post("/archivePolicy", route(archivePolicy));
app.post("/resolveBundle", route(resolveBundle));
app.post("/enrichReport", route(enrichReport));
app.post("/validateThreshold", route(validateThreshold));
app.post("/compactRoster", route(compactRoster));
app.post("/verifyOrder", route(verifyOrder));

app.listen(3000, "0.0.0.0");
