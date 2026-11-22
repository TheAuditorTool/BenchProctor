// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("upload-gateway")
export class ValidateSchedule {
  @Post("validateSchedule")
  async validateSchedule(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = synopsis;
    const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(rendition);
    return { created: true };
  }
}
