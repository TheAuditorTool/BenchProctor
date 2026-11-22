// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("canary-controller")
export class CollectThreshold {
  @Post("collectThreshold")
  async collectThreshold(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const formData = Object.freeze({ payload: remark });
    const note = formData.payload;
    nodeSerialize.unserialize(note);
    return { created: true };
  }
}
