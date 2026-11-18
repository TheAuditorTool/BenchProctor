// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("trace-collector")
export class RotateTrace {
  @Post("rotateTrace")
  async rotateTrace(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(caption);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [cohort] });
    return { created: true };
  }
}
