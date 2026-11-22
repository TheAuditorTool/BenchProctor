// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("canary-controller")
export class RotatePolicy {
  @Post("rotatePolicy")
  async rotatePolicy(@Req() req: Request): Promise<unknown> {
    const remark = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = remark;
    const note = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(note);
    return { created: true };
  }
}
