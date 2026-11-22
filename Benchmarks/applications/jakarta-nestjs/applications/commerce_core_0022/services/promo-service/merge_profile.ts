// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("promo-service")
export class MergeProfile {
  @Post("mergeProfile")
  async mergeProfile(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(subject);
    const voucher: string = readInput();
    const reportSpec = jsYaml.load(String(voucher), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
