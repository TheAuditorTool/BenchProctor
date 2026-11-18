import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { shipLog } from "./log_ship";
import { validateReceipt } from "./validate_receipt";
import { validateBundle } from "./validate_bundle";
import { loadSummary } from "./load_summary";
import { compactThreshold } from "./compact_threshold";
import { fetchIndex } from "./fetch_index";
import { enrichRecord } from "./enrich_record";
import { normalizeSchedule } from "./normalize_schedule";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/shipLog", route(shipLog));
app.post("/validateReceipt", route(validateReceipt));
app.post("/validateBundle", route(validateBundle));
app.post("/loadSummary", route(loadSummary));
app.post("/compactThreshold", route(compactThreshold));
app.post("/fetchIndex", route(fetchIndex));
app.post("/enrichRecord", route(enrichRecord));
app.post("/normalizeSchedule", route(normalizeSchedule));

app.listen(3000, "0.0.0.0");
