// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("ocr-service")
export class PublishCheckpoint {
  @Post("publishCheckpoint")
  async publishCheckpoint(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.authorization as string) || "";
    const _raw = note;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    nodeSerialize.unserialize(addendum);
    return { created: true };
  }
}
