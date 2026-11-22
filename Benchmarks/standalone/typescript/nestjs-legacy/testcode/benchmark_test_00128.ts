// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00128")
  async BenchmarkTest00128(@Headers("host") host: string): Promise<unknown> {
    const userInput = host || "";
    const data = String(userInput).replace(/\u0000/g, "");
    const quantity = parseInt(String(data), 10);
    const totalCents = Math.imul(quantity, 1999);
    return { quantity, totalCents };
  }
}
