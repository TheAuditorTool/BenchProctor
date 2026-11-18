// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00649")
  async BenchmarkTest00649(@Body("multipart_field") mf: string): Promise<unknown> {
    const userInput = mf || "";
    const payload = { get value() { return userInput; } };
    const data = payload.value;
    const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
    return { token };
  }
}
