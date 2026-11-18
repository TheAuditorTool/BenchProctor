// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("metadata-index")
export class FormatCheckpoint {
  @Post("formatCheckpoint")
  async formatCheckpoint(@Req() req: Request): Promise<unknown> {
    const passage = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const montage: string = transform(passage);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [montage] });
    return { created: true };
  }
}
