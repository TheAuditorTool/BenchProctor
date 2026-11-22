import express, { Request, Response } from "express";
import session from "express-session";

import { renderPreview } from "./preview_render";
import { renderLedger } from "./render_ledger";
import { loadConfig } from "./load_config";
import { loadRoster } from "./load_roster";
import { renderSnapshot } from "./render_snapshot";
import { compactLedger } from "./compact_ledger";
import { annotateRecord } from "./annotate_record";
import { formatRevision } from "./format_revision";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/renderPreview/:id", renderPreview);
app.post("/renderLedger", renderLedger);
app.post("/loadConfig", loadConfig);
app.post("/loadRoster", loadRoster);
app.post("/renderSnapshot", renderSnapshot);
app.post("/compactLedger", compactLedger);
app.post("/annotateRecord", annotateRecord);
app.post("/formatRevision", formatRevision);

app.listen(3000, "0.0.0.0");
