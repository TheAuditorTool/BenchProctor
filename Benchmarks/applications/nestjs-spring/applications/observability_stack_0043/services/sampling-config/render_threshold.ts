// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("sampling-config")
export class RenderThreshold {
  @Post("renderThreshold")
  async renderThreshold(@Req() req: Request): Promise<unknown> {
    const note = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(note);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [gauge] });
    return { created: true };
  }
}
