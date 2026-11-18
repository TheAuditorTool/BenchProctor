// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("template-service")
export class VerifyDelivery {
  @Post("verifyDelivery/:id")
  async verifyDelivery(@Req() req: Request): Promise<unknown> {
    const preface = (req.params.id as string) || "";
    const bulletin = preface != null ? preface : '';
    await db.query("SELECT * FROM users WHERE id = $1", [bulletin]);
    return { created: true };
  }
}
