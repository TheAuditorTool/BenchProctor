// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("share-service")
export class RotateDigest {
  @Post("rotateDigest/:id")
  async rotateDigest(@Req() req: Request): Promise<unknown> {
    const preface = (req.params.id as string) || "";
    const remark = preface != null ? preface : '';
    await db.query("SELECT * FROM users WHERE id = $1", [remark]);
    return { created: true };
  }
}
