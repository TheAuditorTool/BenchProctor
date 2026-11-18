// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
import * as net from "net";
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
  @Post("BenchmarkTest00528")
  async BenchmarkTest00528(@Headers("referer") referer: string): Promise<unknown> {
    const userInput = referer || "";
    const data = String(userInput).slice(0, 200);
    net.connect(80, new URL(String(data)).hostname);
    return { created: true };
  }
}
