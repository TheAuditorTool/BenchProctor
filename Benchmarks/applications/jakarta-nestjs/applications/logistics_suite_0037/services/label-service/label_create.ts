// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("label-service")
export class CreateLabel {
  @Post("createLabel")
  async createLabel(@Req() req: Request): Promise<unknown> {
    const memo = req.body.shipping_payload || "";
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [memo] });
    return { created: true };
  }
}
