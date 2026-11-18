// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("retention-service")
export class RotateDigest {
  @Post("rotateDigest/:id")
  async rotateDigest(@Req() req: Request): Promise<unknown> {
    const summary = (req.params.id as string) || "";
    const cohort = summary != null ? summary : '';
    await db.query("SELECT * FROM users WHERE id = $1", [cohort]);
    return { created: true };
  }
}
