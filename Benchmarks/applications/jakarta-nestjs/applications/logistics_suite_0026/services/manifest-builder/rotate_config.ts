// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("manifest-builder")
export class RotateConfig {
  @Post("rotateConfig/:id")
  async rotateConfig(@Req() req: Request): Promise<unknown> {
    const citation = (req.params.id as string) || "";
    const parcel = citation != null ? citation : '';
    await db.query("SELECT * FROM users WHERE id = $1", [parcel]);
    return { created: true };
  }
}
