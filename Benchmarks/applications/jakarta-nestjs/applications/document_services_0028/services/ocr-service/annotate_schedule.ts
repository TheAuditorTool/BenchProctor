// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("ocr-service")
export class AnnotateSchedule {
  @Post("annotateSchedule/:id")
  async annotateSchedule(@Req() req: Request): Promise<unknown> {
    const note = (req.params.id as string) || "";
    const addendum = note != null ? note : '';
    await db.query("SELECT * FROM users WHERE id = $1", [addendum]);
    return { created: true };
  }
}
