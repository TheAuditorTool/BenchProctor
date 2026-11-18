// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, Redirect, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as nodeUtil from "util";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00369")
  @Redirect()
  async BenchmarkTest00369(@Headers("referer") referer: string): Promise<unknown> {
    const userInput = referer || "";
    const data = nodeUtil.format("%s", userInput);
    let _host = "";
    try { _host = new URL(String(data)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const targetUrl = data;
    return { url: targetUrl };
  }
}
