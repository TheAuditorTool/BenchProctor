// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("connector-api")
export class InvokeConnector {
  @Post("invokeConnector")
  async invokeConnector(@Req() req: Request): Promise<unknown> {
    const headline = req.body.integrations_payload || "";
    await db.query("SELECT * FROM users WHERE id = $1", [headline]);
    return { created: true };
  }
}
