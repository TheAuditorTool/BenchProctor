import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { mapField } from "./field_mapping";
import { summarizeHeader } from "./summarize_header";
import { validateMapping } from "./validate_mapping";
import { summarizeThreshold } from "./summarize_threshold";
import { fetchSummary } from "./fetch_summary";
import { collectReport } from "./collect_report";
import { archiveWebhook } from "./archive_webhook";
import { summarizeWebhook } from "./summarize_webhook";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/mapField", route(mapField));
app.post("/summarizeHeader", route(summarizeHeader));
app.post("/validateMapping", route(validateMapping));
app.post("/summarizeThreshold", route(summarizeThreshold));
app.post("/fetchSummary", route(fetchSummary));
app.post("/collectReport", route(collectReport));
app.post("/archiveWebhook", route(archiveWebhook));
app.post("/summarizeWebhook", route(summarizeWebhook));

app.listen(3000, "0.0.0.0");
