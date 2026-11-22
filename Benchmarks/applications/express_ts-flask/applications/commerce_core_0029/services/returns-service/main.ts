import express, { Request, Response } from "express";
import session from "express-session";

import { requestReturn } from "./return_request";
import { archiveWindow } from "./archive_window";
import { normalizeCheckpoint } from "./normalize_checkpoint";
import { validateHeader } from "./validate_header";
import { collectFulfillment } from "./collect_fulfillment";
import { rotateFulfillment } from "./rotate_fulfillment";
import { enrichProfile } from "./enrich_profile";
import { formatHeader } from "./format_header";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/requestReturn", requestReturn);
app.post("/archiveWindow", archiveWindow);
app.post("/normalizeCheckpoint", normalizeCheckpoint);
app.post("/validateHeader", validateHeader);
app.post("/collectFulfillment", collectFulfillment);
app.post("/rotateFulfillment", rotateFulfillment);
app.post("/enrichProfile", enrichProfile);
app.post("/formatHeader", formatHeader);

app.listen(3000, "0.0.0.0");
