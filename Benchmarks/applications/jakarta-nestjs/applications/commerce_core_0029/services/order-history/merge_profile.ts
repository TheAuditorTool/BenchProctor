// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("order-history")
export class MergeProfile {
  @Post("mergeProfile")
  async mergeProfile(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(notice);
    const backorder: string = readInput();
    const reportSpec = jsYaml.load(String(backorder), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
