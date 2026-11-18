// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("connector-api")
export class RenderConfig {
  @Post("renderConfig/:id")
  async renderConfig(@Req() req: Request): Promise<unknown> {
    const snippet = (req.params.id as string) || "";
    const handshake = snippet != null ? snippet : '';
    await db.query("SELECT * FROM users WHERE id = $1", [handshake]);
    return { created: true };
  }
}
