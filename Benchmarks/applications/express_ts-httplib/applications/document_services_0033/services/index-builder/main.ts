import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { indexDocument } from "./search_index";
import { rotateConversion } from "./rotate_conversion";
import { rotateSchedule } from "./rotate_schedule";
import { publishSchedule } from "./publish_schedule";
import { enrichReceipt } from "./enrich_receipt";
import { fetchRecord } from "./fetch_record";
import { renderThreshold } from "./render_threshold";
import { formatProfile } from "./format_profile";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/indexDocument", indexDocument);
app.post("/rotateConversion", rotateConversion);
app.post("/rotateSchedule/:id", rotateSchedule);
app.post("/publishSchedule", publishSchedule);
app.post("/enrichReceipt", enrichReceipt);
app.post("/fetchRecord", fetchRecord);
app.post("/renderThreshold", renderThreshold);
app.post("/formatProfile", formatProfile);

app.listen(3000, "0.0.0.0");
