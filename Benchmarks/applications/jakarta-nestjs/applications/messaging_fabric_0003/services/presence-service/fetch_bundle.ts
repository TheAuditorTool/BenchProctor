// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("presence-service")
export class FetchBundle {
  @Post("fetchBundle/:id")
  async fetchBundle(@Req() req: Request): Promise<unknown> {
    const subject = (req.params.id as string) || "";
    const bulletin = subject != null ? subject : '';
    await db.query("SELECT * FROM users WHERE id = $1", [bulletin]);
    return { created: true };
  }
}
