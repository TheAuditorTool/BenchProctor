// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("session-store")
export class AnnotateDevice {
  @Post("annotateDevice")
  async annotateDevice(@Req() req: Request): Promise<unknown> {
    const tagline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = tagline;
    const persona = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(persona);
    return { created: true };
  }
}
